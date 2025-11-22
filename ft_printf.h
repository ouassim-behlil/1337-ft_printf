/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: obehlil <obehlil@student.1337.ma>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/09 13:18:55 by obehlil           #+#    #+#             */
/*   Updated: 2025/11/17 20:12:56 by obehlil          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <unistd.h>
# include <stdarg.h>

int	ft_printf(const char *str, ...);
int	ft_putchar(int c);
int	ft_putnbr(int n);
int	ft_putstr(const char *str);
int	ft_hexputlower(unsigned int n);
int	ft_hexputupper(unsigned int n);
int	ft_putptr(void *ptr);
int	ft_putunbr(unsigned int n);
int	ft_ptr_hexputlower(unsigned long n);

#endif