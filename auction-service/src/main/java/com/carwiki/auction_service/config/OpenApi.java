package com.carwiki.auction_service.config;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Info;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class OpenApi {

    @Bean
    public OpenAPI customOpenAPI() {
        return  new OpenAPI()
                .info(new Info()
                        .title("Carwiki Auction Service API")
                        .version("1.0.0")
                        .description("API for managing car auctions"));
    }
}
