package com.carwiki.auction_service.service;

import com.carwiki.auction_service.dto.AuctionDto;
import com.carwiki.auction_service.dto.CreateAuctionDto;

import java.util.List;

public interface AuctionService {
    AuctionDto createAuction(CreateAuctionDto auctionDto);

    List<AuctionDto> getAllAuctions();

    AuctionDto getAuctionById(String id);
}
