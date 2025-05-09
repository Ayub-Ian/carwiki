package com.carwiki.search_service.mapper;

import com.carwiki.search_service.dto.ItemDto;
import com.carwiki.search_service.entity.Item;

public class ItemMapper {
    public static ItemDto maptoItemDto(Item item) {
        ItemDto dto = new ItemDto();
        dto.setId(item.getId());
        dto.setColor(item.getColor());
        dto.setMake(item.getMake());
        dto.setMileage(item.getMileage());
        dto.setSeller(item.getSeller());
        dto.setAuctionEnd(item.getAuctionEnd());
        dto.setCreatedAt(item.getCreatedAt());
        dto.setCurrentHighBid(item.getCurrentHighBid());
        dto.setImageUrl(item.getImageUrl());
        dto.setModel(item.getModel());
        dto.setWinner(item.getWinner());
        dto.setUpdatedAt(item.getUpdatedAt());
        dto.setReservePrice(item.getReservePrice());
        dto.setSoldAmount(item.getSoldAmount());
        dto.setStatus(item.getStatus());
        dto.setYear(item.getYear());
        return dto;
    }
}
