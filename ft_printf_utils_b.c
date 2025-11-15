/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_utils_b.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: obehlil <obehlil@student.1337.ma>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/09 21:17:18 by obehlil           #+#    #+#             */
/*   Updated: 2025/11/09 21:18:37 by obehlil          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_hexputupper(unsigned int n)
{
	int			count;

	count = 0;
	if (n >= 16)
		count += ft_hexputupper(n / 16);
	count += ft_putchar("0123456789ABCDEF"[n % 16]);
	return (count);
}

int	ft_ptr_hexputlower(unsigned long n)
{
	int			count;

	count = 0;
	if (n >= 16)
		count += ft_ptr_hexputlower(n / 16);
	count += ft_putchar("0123456789abcdef"[n % 16]);
	return (count);
}

int	ft_putptr(void *ptr)
{
	unsigned long	nb;
	int				count;

	if (!ptr)
		return (ft_putstr("(nil)"));
	count = 0;
	nb = (unsigned long)ptr;
	count += write(1, "0x", 2);
	count += ft_ptr_hexputlower(nb);
	return (count);
}
