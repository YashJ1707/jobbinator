package io.jobbinator_server.DTO;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotNull;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString
public class AuthDTO {
    @NotNull
    @Email(message = "Enter correct email")
    private String email;
    @NotNull
    private String hash;
}
