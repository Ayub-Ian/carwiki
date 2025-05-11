package com.carwiki.auction_service.controller;

import com.carwiki.auction_service.dto.AuctionDto;
import com.carwiki.auction_service.dto.CreateAuctionDto;
import com.carwiki.auction_service.exception.ResourceNotFoundException;
import com.carwiki.auction_service.service.AuctionService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import jakarta.validation.Valid;
import java.util.List;

@AllArgsConstructor
@RestController
@RequestMapping("api/auctions")
@Tag(name = "Auctions", description = "Operations related to car auctions")
public class AuctionController {

    private AuctionService auctionService;

    @Operation(summary = "Create a new car auction", description = "Creates a new auction with the provided car details and auction parameters")
    @ApiResponses(value = {
            @ApiResponse(responseCode = "201", description = "Auction created successfully"),
            @ApiResponse(responseCode = "400", description = "Invalid input data"),
            @ApiResponse(responseCode = "500", description = "Internal server error")
    })
    @PostMapping
    public ResponseEntity<AuctionDto> createAuction(@Valid @RequestBody CreateAuctionDto createAuctionDto) {
        AuctionDto createdAuction = auctionService.createAuction(createAuctionDto);
        return new ResponseEntity<>(createdAuction, HttpStatus.CREATED);
    }

    @Operation(summary = "Retrieve all auctions", description = "Fetches a list of all active and completed auctions")
    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "List of auctions retrieved successfully"),
            @ApiResponse(responseCode = "500", description = "Internal server error")
    })
    @GetMapping
    public ResponseEntity<List<AuctionDto>> fetchAllAuctions() {
        List<AuctionDto> auctionDtos = auctionService.getAllAuctions();
        return new ResponseEntity<>(auctionDtos, HttpStatus.OK);
    }

    @Operation(summary = "Get auction by ID", description = "Retrieves details of a specific auction by its unique identifier")
    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "Auction details retrieved successfully"),
            @ApiResponse(responseCode = "404", description = "Auction not found"),
            @ApiResponse(responseCode = "500", description = "Internal server error")
    })
    @GetMapping("/{id}")
    public ResponseEntity<AuctionDto> getAuctionById(@PathVariable("id") String id) {
        AuctionDto auction = auctionService.getAuctionById(id);
        return new ResponseEntity<>(auction, HttpStatus.OK);
    }

    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<String> handleAuctionNotFound(ResourceNotFoundException ex) {
        return new ResponseEntity<>(ex.getMessage(), HttpStatus.NOT_FOUND);
    }
}