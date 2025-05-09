package com.carwiki.search_service.service;

import com.carwiki.search_service.dto.SearchParams;

import java.util.Map;

public interface SearchService {
    Map<String, Object> searchItems(SearchParams searchParams);
}
