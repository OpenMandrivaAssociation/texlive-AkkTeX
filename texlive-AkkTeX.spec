Name:		texlive-AkkTeX
Version:	26055
Release:	1
Summary:	A collection of packages and classes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/akktex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/akktex.r26055.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/akktex.doc.r26055.tar.xz
BuildArch:	noarch
Provides:	texlive-akktex
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides: - new document classes for technical
documents, thesis works, manuscripts and lecture notes; - many
mathematical packages providing a large number of macros for
mathematical texts; - layout providing a non-empty parskip with
extended length corrections and new section definition
commands; - easy label creation for counters; and - german
language tools and predefined abbreviations.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/akktex
%doc %{_texmfdistdir}/doc/latex/akktex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
