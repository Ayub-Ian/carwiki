package com.carwiki.auction_service.mapper;

import com.carwiki.auction_service.dto.CreateAuctionDto;
import com.carwiki.auction_service.entity.Auction;
import com.carwiki.auction_service.entity.Item;

public class CreateAuctionMapper {

    // Maps DTO to Auction entity first then to Item entity
    public static Auction mapToAuction(CreateAuctionDto createAuctionDto) {
        Auction auction = new Auction();
        auction.setAuctionEnd(createAuctionDto.getAuctionEnd());
        auction.setReservePrice(createAuctionDto.getReservePrice());
        return auction;
    }

    public static Item mapToItem(CreateAuctionDto createAuctionDto, Auction auction) {
        Item item = new Item();
        item.setMake(createAuctionDto.getMake());
        item.setColor(createAuctionDto.getColor());
        item.setMileage(createAuctionDto.getMileage());
        item.setModel(createAuctionDto.getModel());
        item.setYear(createAuctionDto.getYear());
        item.setImageUrl(createAuctionDto.getImageUrl());

        item.setAuction(auction);
        return item;
    }
}
