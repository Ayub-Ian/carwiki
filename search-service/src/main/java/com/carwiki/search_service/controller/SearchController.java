package com.carwiki.search_service.controller;

import com.carwiki.search_service.dto.SearchParams;
import com.carwiki.search_service.exception.ResourceNotFoundException;
import com.carwiki.search_service.service.SearchService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;



import java.util.Map;

@RestController
@RequestMapping("/api/search")
public class SearchController {

    private final SearchService searchService;

    public SearchController(SearchService searchService) {
        this.searchService = searchService;
    }

    @GetMapping
    public ResponseEntity<Map<String, Object>> searchItems(SearchParams searchParams) {
        return ResponseEntity.ok(searchService.searchItems(searchParams));
    }

    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<String> handleAuctionNotFound(ResourceNotFoundException ex) {
        return new ResponseEntity<>(ex.getMessage(), HttpStatus.NOT_FOUND);
    }
}