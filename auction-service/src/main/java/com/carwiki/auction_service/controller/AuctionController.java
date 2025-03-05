package com.carwiki.auction_service.controller;

import com.carwiki.auction_service.dto.AuctionDto;
import com.carwiki.auction_service.dto.CreateAuctionDto;
import com.carwiki.auction_service.exception.ResourceNotFoundException;
import com.carwiki.auction_service.service.AuctionService;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@AllArgsConstructor
@RestController
@RequestMapping("api/auctions")
public class AuctionController {

    private AuctionService auctionService;

    @PostMapping
    public ResponseEntity<AuctionDto> createAuction(@RequestBody CreateAuctionDto createAuctionDto){
        AuctionDto createdAuction = auctionService.createAuction(createAuctionDto);
        return new ResponseEntity<>(createdAuction,HttpStatus.CREATED);
    }

    @GetMapping
    public ResponseEntity<List<AuctionDto>> fetchAllAuctions() {
        List<AuctionDto> auctionDtos = auctionService.getAllAuctions();
        return new ResponseEntity<>(auctionDtos, HttpStatus.OK);
    }

    @GetMapping("{id}")
    public ResponseEntity<AuctionDto> getAuctionById(@PathVariable("id") String id) {
        AuctionDto auction = auctionService.getAuctionById(id);
        return new ResponseEntity<>(auction, HttpStatus.OK);
    }

    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<String> handleAuctionNotFound(ResourceNotFoundException ex) {
        return new ResponseEntity<>(ex.getMessage(), HttpStatus.NOT_FOUND);
    }

}
