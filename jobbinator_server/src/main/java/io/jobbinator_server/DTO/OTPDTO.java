package io.jobbinator_server.DTO;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotNull;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;


@Getter
@Setter
@ToString
public class OTPDTO {
    @Email
    @NotNull
    private String email;
    @NotNull(message = "OTP should not be empty")
    private String otp;
    }