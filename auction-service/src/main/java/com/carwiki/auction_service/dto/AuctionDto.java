package com.carwiki.auction_service.dto;

import com.carwiki.auction_service.entity.Item;
import com.carwiki.auction_service.entity.Status;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDateTime;
import java.util.UUID;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class AuctionDto {
    private String id;
    private int reservePrice;
    private String seller;
    private String winner;
    private Integer soldAmount;
    private Integer currentHighBid;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
    private LocalDateTime auctionEnd;
    private String status;
    private String make;
    private String model;
    private int year;
    private String color;
    private int mileage;
    private String imageUrl;
}
