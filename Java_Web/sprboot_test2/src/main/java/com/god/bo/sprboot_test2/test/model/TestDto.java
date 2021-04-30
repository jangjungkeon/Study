package com.god.bo.sprboot_test2.test.model;

public class TestDto {
    private Long mbrNo;
    private String id;
    private String name;

    public TestDto(){}

    public TestDto(String id, String name){
        this.id = id;
        this.name = name;
    }

    public Long getMbrNo() {
        return mbrNo;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public void setMbrNo(Long mbrNo) {
        this.mbrNo = mbrNo;
    }

    public void setId(String id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }
}
