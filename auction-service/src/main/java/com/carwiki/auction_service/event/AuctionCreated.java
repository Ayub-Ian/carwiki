package com.carwiki.auction_service.event;

import com.carwiki.auction_service.dto.AuctionDto;

public class AuctionCreated {
    private final AuctionDto payload;

    public AuctionCreated(AuctionDto payload) {
        this.payload = payload;
    }

    public String getEventType() {
        return "AuctionCreated";
    }

    public AuctionDto getPayload() {
        return payload;
    }
}