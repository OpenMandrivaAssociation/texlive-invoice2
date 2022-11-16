Name:		texlive-invoice2
Version:	46364
Release:	1
Summary:	Intelligent invoices with LaTeX3
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/invoice2
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/invoice2.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/invoice2.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/invoice2.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Typeset invoices with automatic VAT and calculation of totals.
Supports internationalization, invoices are typeset with
booktabs for readability. Does not support separate projects
per invoice. Can be used as a replacement for invoice in most
cases.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/invoice2
%{_texmfdistdir}/tex/latex/invoice2
%doc %{_texmfdistdir}/doc/latex/invoice2

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
