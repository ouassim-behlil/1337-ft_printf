/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_utils_a.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: obehlil <obehlil@student.1337.ma>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/09 15:21:04 by obehlil           #+#    #+#             */
/*   Updated: 2025/11/09 21:19:58 by obehlil          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putchar(int c)
{
	unsigned char	uc;

	uc = (unsigned char)c;
	return (write(1, &uc, 1));
}

int	ft_putnbr(int n)
{
	long		nb;
	int			count;

	nb = (long)n;
	count = 0;
	if (nb < 0)
	{
		count += ft_putchar('-');
		nb = -nb;
	}
	if (nb >= 10)
		count += ft_putnbr(nb / 10);
	count += ft_putchar('0' + (nb % 10));
	return (count);
}

int	ft_putunbr(unsigned int n)
{
	int			count;

	count = 0;
	if (n >= 10)
		count += ft_putunbr(n / 10);
	count += ft_putchar('0' + (n % 10));
	return (count);
}

int	ft_putstr(const char *str)
{
	int			ind;

	if (!str)
		return (ft_putstr("(null)"));
	ind = 0;
	while (str[ind])
		ft_putchar(str[ind++]);
	return (ind);
}

int	ft_hexputlower(unsigned int n)
{
	int			count;

	count = 0;
	if (n >= 16)
		count += ft_hexputlower(n / 16);
	count += ft_putchar("0123456789abcdef"[n % 16]);
	return (count);
}
