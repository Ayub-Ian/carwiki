package com.carwiki.auction_service.mapper;

import com.carwiki.auction_service.dto.AuctionDto;
import com.carwiki.auction_service.entity.Auction;
import com.carwiki.auction_service.entity.Item;

public class AuctionMapper {

    public static AuctionDto maptoAuctionDto(Auction auction, Item item) {
        AuctionDto dto = new AuctionDto();
        dto.setId(auction.getId().toString());
        dto.setReservePrice(auction.getReservePrice());
        dto.setSeller(auction.getSeller());
        dto.setWinner(auction.getWinner());
        dto.setSoldAmount(auction.getSoldAmount());
        dto.setCurrentHighBid(auction.getHighestBid());
        dto.setCreatedAt(auction.getCreatedAt());
        dto.setUpdatedAt(auction.getUpdatedAt());
        dto.setAuctionEnd(auction.getAuctionEnd());
        dto.setStatus(String.valueOf(auction.getStatus()));
        dto.setMake(item.getMake());
        dto.setModel(item.getModel());
        dto.setYear(item.getYear());
        dto.setColor(item.getColor());
        dto.setMileage(item.getMileage());
        dto.setImageUrl(item.getImageUrl());
        return dto;
    }


}
