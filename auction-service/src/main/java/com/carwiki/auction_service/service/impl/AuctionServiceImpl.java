package com.carwiki.auction_service.service.impl;

import com.carwiki.auction_service.dto.AuctionDto;
import com.carwiki.auction_service.dto.CreateAuctionDto;
import com.carwiki.auction_service.entity.Auction;
import com.carwiki.auction_service.entity.Item;
import com.carwiki.auction_service.exception.ResourceNotFoundException;
import com.carwiki.auction_service.mapper.AuctionMapper;
import com.carwiki.auction_service.mapper.CreateAuctionMapper;
import com.carwiki.auction_service.repository.AuctionRepository;
import com.carwiki.auction_service.repository.ItemRepository;
import com.carwiki.auction_service.service.AuctionService;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
@AllArgsConstructor
public class AuctionServiceImpl implements AuctionService {

    private AuctionRepository auctionRepository;
    private ItemRepository itemRepository;


    @Override
    public AuctionDto createAuction(CreateAuctionDto createAuctionDto) {

        Auction newAuction = CreateAuctionMapper.mapToAuction(createAuctionDto);
        newAuction.setCreatedAt(LocalDateTime.now());
        newAuction.setUpdatedAt(LocalDateTime.now());
        Auction savedAuction = auctionRepository.save(newAuction);

        Item newitem = CreateAuctionMapper.mapToItem(createAuctionDto, savedAuction);
        Item savedItem = itemRepository.save(newitem);

        return AuctionMapper.maptoAuctionDto(savedAuction, savedItem);
    }

    @Override
    public List<AuctionDto> getAllAuctions() {
        List<Auction> auctions = auctionRepository.findAllWithItems();
        return auctions.stream().map((auction) ->
                AuctionMapper.maptoAuctionDto(auction, auction.getItem())).collect(Collectors.toList());

    }

    @Override
    public AuctionDto getAuctionById(String id) {
        UUID auctionId = UUID.fromString(id);
        Auction auction = auctionRepository.findByIdWithItem(auctionId).orElseThrow(() ->
                new ResourceNotFoundException("Auction not found with id " + id));

        return AuctionMapper.maptoAuctionDto(auction,auction.getItem());
    }


}
