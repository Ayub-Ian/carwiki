package com.carwiki.search_service.dto;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;

@Data
@Schema(description = "Parameters for searching auction items")
public class SearchParams {
    @Schema(description = "Search term for full-text search on make and model", example = "Audi")
    private String searchTerm;

    @Schema(description = "Sort order: 'make', 'new', or default ('auctionEnd')", example = "make")
    private String orderBy;

    @Schema(description = "Filter by auction status: 'finished', 'endingSoon', or 'live'", example = "live")
    private String filterBy;

    @Schema(description = "Filter by seller username", example = "bob")
    private String seller;

    @Schema(description = "Filter by winner username", example = "alice")
    private String winner;

    @Schema(description = "Page number (1-based)", example = "1", minimum = "1")
    private int pageNumber = 1;

    @Schema(description = "Number of items per page", example = "10", minimum = "1")
    private int pageSize = 10;
}