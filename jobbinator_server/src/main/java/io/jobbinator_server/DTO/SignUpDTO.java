package io.jobbinator_server.DTO;

import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.Column;
import jakarta.validation.constraints.NotNull;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.sql.Date;

@Getter
@Setter
@ToString
public class SignUpDTO {
    @NotNull
    private String name;
    @NotNull
    private Integer age;
    @NotNull
    private String gender;
    @NotNull
    private Date dob;
    @NotNull
    private Integer number;
    @NotNull
    private String email;
    @NotNull
    private String hash;

}
