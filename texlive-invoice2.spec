%global tl_name invoice2
%global tl_revision 67327

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Intelligent invoices with LaTeX3
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/invoice2
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/invoice2.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/invoice2.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/invoice2.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(booktabs)
Requires:	texlive(l3kernel)
Requires:	texlive(l3packages)
Requires:	texlive(siunitx)
Requires:	texlive(tools)
Requires:	texlive(translations)
Requires:	texlive(xcolor)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Typeset invoices with automatic VAT and calculation of totals. Supports
internationalization, invoices are typeset with booktabs for
readability. Does not support separate projects per invoice. Can be used
as a replacement for invoice in most cases.

