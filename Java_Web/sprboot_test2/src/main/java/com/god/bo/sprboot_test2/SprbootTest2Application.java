package com.god.bo.sprboot_test2;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
// @SpringBootApplication = @EnableAutoConfiguration + @ComponentScan + @Configuration
// @SpringBootApplication 를 설정한 클래스가 있는 package 를 최상위 패키지로 인식하고 ComponentScan를 수행
// 즉, 현재 패키지를 최상위 패키지로 인식.
public class SprbootTest2Application {

    public static void main(String[] args) {

        SpringApplication.run(SprbootTest2Application.class, args);
    }

}
