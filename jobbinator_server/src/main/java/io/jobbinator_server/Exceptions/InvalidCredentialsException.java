package io.jobbinator_server.Exceptions;

import org.springframework.security.core.AuthenticationException;

public class InvalidCredentialsException extends AuthenticationException {
    public InvalidCredentialsException(String message) {
        super(message);
    }
}
