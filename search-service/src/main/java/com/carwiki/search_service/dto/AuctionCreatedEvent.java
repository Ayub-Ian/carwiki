package com.carwiki.search_service.dto;

import lombok.Data;

@Data
public class AuctionCreatedEvent {
    private ItemDto payload;
    private String eventType;
}