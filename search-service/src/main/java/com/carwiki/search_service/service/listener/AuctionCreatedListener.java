package com.carwiki.search_service.service.listener;

import com.carwiki.search_service.dto.AuctionCreatedEvent;
import com.carwiki.search_service.dto.ItemDto;
import com.carwiki.search_service.entity.Item;
import com.carwiki.search_service.mapper.ItemMapper;
import com.carwiki.search_service.repository.ItemRepository;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

@Slf4j
@Component
@RequiredArgsConstructor
public class AuctionCreatedListener {

    private final ItemRepository itemRepository;
    private final ObjectMapper objectMapper;

    public void handleMessage(String message) {
        try {
            log.info("Received message from auction:created channel: {}", message);
            AuctionCreatedEvent event = objectMapper.readValue(message, AuctionCreatedEvent.class);
            ItemDto itemDto = event.getPayload();
            if (itemDto == null) {
                log.error("ItemDto payload is null in message: {}", message);
                return;
            }
            Item item = ItemMapper.mapToItem(itemDto);
            itemRepository.save(item);
            log.info("Saved item to MongoDB: {}", item.getId());
        } catch (Exception e) {
            log.error("Failed to process auction:created message: {}", message, e);
        }
    }
}