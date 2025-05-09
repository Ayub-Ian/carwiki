package com.carwiki.search_service.dto;

import lombok.Data;

@Data
public class SearchParams {
    private String searchTerm;
    private String orderBy;
    private String filterBy;
    private String seller;
    private String winner;
    private int pageNumber = 1;
    private int pageSize = 10;
}
