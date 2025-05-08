package com.carwiki.search_service.data;

import com.carwiki.search_service.entity.Item;
import com.carwiki.search_service.repository.ItemRepository;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ClassPathResource;

import java.io.InputStream;
import java.util.List;

@Configuration
public class DataSeeder {

    @Autowired
    private ItemRepository itemRepository;

    @Bean
    CommandLineRunner seedDatabase() {
        return args -> {
            if (itemRepository.count() == 0) {
                try {
                    ObjectMapper objectMapper = new ObjectMapper();
                    objectMapper.registerModule(new JavaTimeModule());
                    InputStream inputStream = new ClassPathResource("items.json").getInputStream();
                    List<Item> items = objectMapper.readValue(inputStream, new TypeReference<List<Item>>() {});
                    itemRepository.saveAll(items);
                    System.out.println("Successfully seeded " + items.size() + " items into MongoDB.");
                } catch (Exception e) {
                    System.err.println("Failed to seed database: " + e.getMessage());
                }
            } else {
                System.out.println("Database already contains data. Skipping seeding.");
            }
        };
    }
}