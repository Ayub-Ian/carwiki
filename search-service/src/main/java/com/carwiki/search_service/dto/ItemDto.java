package com.carwiki.search_service.dto;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;

import java.time.LocalDateTime;


@Data
@Schema(description = "Data transfer object for an auction item")
public class ItemDto {
    @Schema(description = "Unique identifier of the item", example = "6a5011a1-fe1f-47df-9a32-b5346b289391")
    private String id;

    @Schema(description = "Username of the seller", example = "bob")
    private String seller;

    @Schema(description = "Username of the winner (if auction ended)", example = "alice")
    private String winner;

    @Schema(description = "Car manufacturer", example = "Audi")
    private String make;

    @Schema(description = "Car model", example = "R8")
    private String model;

    @Schema(description = "Manufacturing year", example = "2021")
    private Integer year;

    @Schema(description = "Car color", example = "White")
    private String color;

    @Schema(description = "Car mileage in kilometers", example = "10050")
    private Integer mileage;

    @Schema(description = "URL of the car image", example = "https://cdn.pixabay.com/photo/2019/12/26/20/50/audi-r8-4721217_960_720.jpg")
    private String imageUrl;

    @Schema(description = "Auction status (e.g., 'Live', 'Ended')", example = "Live")
    private String status;

    @Schema(description = "Reserve price of the auction", example = "0")
    private Integer reservePrice;

    @Schema(description = "Final sold amount (if sold)", example = "50000")
    private Integer soldAmount;

    @Schema(description = "Current highest bid (if any)", example = "45000")
    private Integer currentHighBid;

    @Schema(description = "Creation timestamp", example = "2024-08-10T13:57:50.178975Z")
    private LocalDateTime createdAt;

    @Schema(description = "Last update timestamp", example = "2024-08-10T13:57:50.178975Z")
    private LocalDateTime updatedAt;

    @Schema(description = "Auction end timestamp", example = "2024-08-29T13:57:50.178976Z")
    private LocalDateTime auctionEnd;
}