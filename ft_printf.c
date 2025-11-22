/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: obehlil <obehlil@student.1337.ma>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/09 13:20:59 by obehlil           #+#    #+#             */
/*   Updated: 2025/11/17 20:30:25 by obehlil          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	is_format_specifier(char c)
{
	if (c == 'd' || c == 'u' || c == 'c' || c == 's' \
	|| c == 'p' || c == 'x' || c == 'X' || c == 'i' || c == '%')
		return (1);
	return (0);
}

static int	convert(const char c, va_list *ap)
{
	if (c == 'c')
		return (ft_putchar(va_arg(*ap, int)));
	else if (c == 'd' || c == 'i')
		return (ft_putnbr(va_arg(*ap, int)));
	else if (c == 'p')
		return (ft_putptr(va_arg(*ap, void *)));
	else if (c == 'u')
		return (ft_putunbr(va_arg(*ap, unsigned int)));
	else if (c == 's')
		return (ft_putstr(va_arg(*ap, char *)));
	else if (c == 'x')
		return (ft_hexputlower(va_arg(*ap, int)));
	else if (c == 'X')
		return (ft_hexputupper(va_arg(*ap, int)));
	else
		return ((int)write(1, &c, 1));
}

static int	process_str(const char *str, va_list *ap)
{
	int				num_printed;
	int				ind;

	num_printed = 0;
	ind = 0;
	while (str[ind])
	{
		if (str[ind] == '%' && str[ind + 1] && is_format_specifier(str[ind + 1]))
			num_printed += convert(str[ind++ + 1], ap);
		else
			num_printed += write(1, &str[ind], 1);
		ind++;
	}
	return (num_printed);
}

int	ft_printf(const char *str, ...)
{
	va_list			ap;
	int				num_printed;

	if (!str)
		return (-1);
	va_start(ap, str);
	num_printed = process_str(str, &ap);
	va_end(ap);
	return (num_printed);
}
