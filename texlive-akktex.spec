%global tl_name akktex
%global tl_revision 26055

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3.2
Release:	%{tl_revision}.1
Summary:	A collection of packages and classes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/akktex
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/akktex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/akktex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides: new document classes for technical documents,
thesis works, manuscripts and lecture notes; many mathematical packages
providing a large number of macros for mathematical texts; layout
providing a non-empty parskip with extended length corrections and new
section definition commands; easy label creation for counters; and
german language tools and predefined abbreviations.

