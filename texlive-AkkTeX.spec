Name:		texlive-AkkTeX
Version:	0.3.2
Release:	1
Summary:	A collection of packages and classes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive//macros/latex/contrib/akktex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/AkkTeX.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/AkkTeX.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The bundle provides: - new document classes for technical
documents, thesis works, manuscripts and lecture notes; - many
mathematical packages providing a large number of macros for
mathematical texts; - layout providing a non-empty parskip with
extended length corrections and new section definition
commands; - easy label creation for counters; and - german
language tools and predefined abbreviations.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/AkkTeX/akkconditional.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akkcounterlabelpattern.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akkcs.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akkdoc.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akkgerman.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akkgermanabbreviations.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akklecture.cls
%{_texmfdistdir}/tex/latex/AkkTeX/akklongpage.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akkmath.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akkmathbasic.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akkmathdisc.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akkmathfun.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akkmathnum.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akkmathpaper.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akkmathproof.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akkmathrel.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akkmathset.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akkmathtext.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akknum.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akkparskip.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akkscript.cls
%{_texmfdistdir}/tex/latex/AkkTeX/akksection.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akkstring.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akktecdoc.cls
%{_texmfdistdir}/tex/latex/AkkTeX/akktex.sty
%{_texmfdistdir}/tex/latex/AkkTeX/akkwidepage.sty
%doc %{_texmfdistdir}/doc/latex/AkkTeX/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
