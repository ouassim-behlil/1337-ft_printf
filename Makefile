SRC = ft_printf.c ft_printf_utils_a.c ft_printf_utils_b.c
OBJ = $(SRC:.c=.o)
HEADER = ft_printf.h
CFLAGS = -Wextra -Wall -Werror
NAME = libftprintf.a

all:	$(NAME)

$(NAME):	$(OBJ)
	ar -rcs $(NAME) $(OBJ)

%.o:	%.c $(HEADER)
	cc $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJ)

fclean:	clean
	rm -rf $(NAME)

re:	fclean all

.PHONY:	all $(NAME) clean fclean re

