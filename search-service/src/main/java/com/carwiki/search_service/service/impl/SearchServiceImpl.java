package com.carwiki.search_service.service.impl;

import com.carwiki.search_service.dto.ItemDto;
import com.carwiki.search_service.dto.SearchParams;
import com.carwiki.search_service.entity.Item;
import com.carwiki.search_service.mapper.ItemMapper;
import com.carwiki.search_service.service.SearchService;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.data.mongodb.core.query.TextCriteria;
import org.springframework.data.mongodb.core.query.TextQuery;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@Service
public class SearchServiceImpl implements SearchService {

    private final MongoTemplate mongoTemplate;

    public SearchServiceImpl(MongoTemplate mongoTemplate) {
        this.mongoTemplate = mongoTemplate;
    }


    @Override
    public Map<String, Object> searchItems(SearchParams searchParams) {
        Query query = new Query();

        // Full-text search
        if (searchParams.getSearchTerm() != null && !searchParams.getSearchTerm().isEmpty()) {
            TextCriteria textCriteria = TextCriteria.forDefaultLanguage().matching(searchParams.getSearchTerm());
            query = TextQuery.queryText(textCriteria).sortByScore();
        }

        // Sorting
        Sort sort = switch (searchParams.getOrderBy() != null ? searchParams.getOrderBy() : "") {
            case "make" -> Sort.by(Sort.Direction.ASC, "make", "model");
            case "new" -> Sort.by(Sort.Direction.DESC, "createdAt");
            default -> Sort.by(Sort.Direction.ASC, "auctionEnd");
        };
        query.with(sort);

        // Filtering
        if (searchParams.getFilterBy() != null && !searchParams.getFilterBy().isEmpty()) {
            LocalDateTime now = LocalDateTime.now();
            switch (searchParams.getFilterBy()) {
                case "finished" -> query.addCriteria(Criteria.where("auctionEnd").lt(now));
                case "endingSoon" -> query.addCriteria(Criteria.where("auctionEnd")
                        .lt(now.plusHours(6))
                        .gt(now));
                default -> query.addCriteria(Criteria.where("auctionEnd").gt(now)); // live
            }
        }

        // Seller filter
        if (searchParams.getSeller() != null && !searchParams.getSeller().isEmpty()) {
            query.addCriteria(Criteria.where("seller").is(searchParams.getSeller()));
        }

        // Winner filter
        if (searchParams.getWinner() != null && !searchParams.getWinner().isEmpty()) {
            query.addCriteria(Criteria.where("winner").is(searchParams.getWinner()));
        }

        // Pagination
        Pageable pageable = PageRequest.of(
                Math.max(0, searchParams.getPageNumber() - 1),
                searchParams.getPageSize()
        );
        query.with(pageable);

        long totalCount = mongoTemplate.count(query, Item.class);
        List<Item> items = mongoTemplate.find(query, Item.class);

        List<ItemDto> results = items.stream()
                .map(ItemMapper::maptoItemDto)
                .collect(Collectors.toList());
        long pageCount = (totalCount + searchParams.getPageSize() - 1) / searchParams.getPageSize();

        Map<String, Object> response = new HashMap<>();
        response.put("results", results);
        response.put("pageCount", pageCount);
        response.put("totalCount", totalCount);

        return response;
    }
}
