package com.carwiki.search_service.controller;

import com.carwiki.search_service.dto.SearchParams;
import com.carwiki.search_service.exception.ResourceNotFoundException;
import com.carwiki.search_service.service.SearchService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.media.*;
import io.swagger.v3.oas.annotations.responses.*;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;



import java.util.Map;

@RestController
@RequestMapping("/api/search")
@Tag(name = "Search", description = "API for searching car auction items")
public class SearchController {

    private final SearchService searchService;

    public SearchController(SearchService searchService) {
        this.searchService = searchService;
    }

    @GetMapping
    @Operation(summary = "Search auction items", description = "Search for car auction items with filtering, sorting, and pagination")
    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "Successful search",
                    content = @Content(mediaType = "application/json",
                            schema = @Schema(implementation = Map.class))),
            @ApiResponse(responseCode = "404", description = "Resource not found",
                    content = @Content(mediaType = "application/json",
                            schema = @Schema(implementation = Map.class))),
            @ApiResponse(responseCode = "500", description = "Internal server error",
                    content = @Content(mediaType = "application/json",
                            schema = @Schema(implementation = Map.class)))
    })
    public ResponseEntity<Map<String, Object>> searchItems(
            @Parameter(description = "Search parameters including search term, filters, and pagination")
            SearchParams searchParams) {
        return ResponseEntity.ok(searchService.searchItems(searchParams));
    }

    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<String> handleAuctionNotFound(ResourceNotFoundException ex) {
        return new ResponseEntity<>(ex.getMessage(), HttpStatus.NOT_FOUND);
    }
}