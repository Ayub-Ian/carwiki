package com.carwiki.auction_service.service;

import com.carwiki.auction_service.event.AuctionCreated;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

@Service
public class EventPublisherService {
    private final RedisTemplate<String, String> redisTemplate;
    private final ObjectMapper objectMapper;
    private static final String AUCTION_CREATED_CHANNEL = "auction:created";


    public EventPublisherService(RedisTemplate<String, String> redisTemplate, ObjectMapper objectMapper) {
        this.redisTemplate = redisTemplate;
        this.objectMapper = objectMapper;
    }

    public void publishAuctionCreatedEvent(AuctionCreated event) {
        try {
            String message = objectMapper.writeValueAsString(event);
            redisTemplate.convertAndSend(AUCTION_CREATED_CHANNEL, message);
        } catch (JsonProcessingException e) {
            throw new RuntimeException("Failed to serialize AuctionCreatedEvent", e);
        }
    }
}