package com.carwiki.search_service.dto;

import lombok.Data;

import java.time.LocalDateTime;


@Data
public class ItemDto {
    private  String id;
    private  String seller;
    private String winner;
    private String make;
    private String model;
    private Integer year;
    private String color;
    private Integer mileage;
    private String imageUrl;
    private  String status;
    private Integer reservePrice;
    private Integer soldAmount;
    private Integer currentHighBid;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
    private LocalDateTime auctionEnd;
}
