Name:           nvidia-sdk-video-codec
Version:        12.0.16
Release:        1%{?dist}
Epoch:          1
Summary:        A comprehensive set of APIs for hardware accelerated video encode and decode
License:        DESIGNWORKS NVIDIA SDKS, SAMPLES AND TOOLS AGREEMENT, DISTRIBUTION RIGHTS (V.13.06.2017)
URL:            https://developer.nvidia.com/nvidia-video-codec-sdk
BuildArch:      noarch

Source0:        Video_Codec_Interface_%{version}.zip
Source1:        https://developer.download.nvidia.com/designworks/DesignWorks_SDKs_Samples_Tools_License_distrib_use_rights_2017_06_13.pdf

Conflicts:      nvidia-video-codec-sdk

Obsoletes:      nvenc < %{?epoch}:%{version}-%{release}
Provides:       nvenc = %{?epoch}:%{version}-%{release}

# Required for:
# - libnvcuvid.so (NVDECODE)
# - libnvidia-encode.so (NVENCODE)
Requires:       nvidia-driver >= 3:520.56.06

%description
The SDK consists of two hardware acceleration interfaces:

    NVENCODE API for video encode acceleration
    NVDECODE API for video decode acceleration

NVIDIA GPUs contain one or more hardware-based decoder and encoder(s) (separate
from the CUDA cores) which provides fully-accelerated hardware-based video
decoding and encoding for several popular codecs. With decoding/encoding
offloaded, the graphics engine and the CPU are free for other operations.

GPU hardware accelerator engines for video decoding (referred to as NVDEC) and
video encoding (referred to as NVENC) support faster than real-time video
processing which makes them suitable to be used for transcoding applications, in
addition to video playback.

%prep
%setup -q -n Video_Codec_Interface_%{version}
cp %{SOURCE1} .

%install
mkdir -p %{buildroot}%{_includedir}/%{name}/
install -m 644 -p Interface/* %{buildroot}%{_includedir}/%{name}/

%files
%license DesignWorks_SDKs_Samples_Tools_License_distrib_use_rights_2017_06_13.pdf
%doc ReadMe.pdf
%{_includedir}/%{name}
 
%changelog
* Mon Feb 06 2023 Simone Caronni <negativo17@gmail.com> - 1:12.0.16-1
- Update to 12.0.16.
- Switch to headers only package, drop samples.

* Wed Sep 22 2021 Simone Caronni <negativo17@gmail.com> - 1:11.1.5-1
- Update to 11.1.5.

* Tue Aug 25 2020 Simone Caronni <negativo17@gmail.com> - 1:10.0.26-2
- Rename to nvidia-video-codec-sdk.

* Fri Jul 10 2020 Simone Caronni <negativo17@gmail.com> - 1:10.0.26-1
- Update to 10.0.26.

* Mon Sep 30 2019 Simone Caronni <negativo17@gmail.com> - 1:9.1.23-1
- Update to 9.1.23.

* Sun Feb 24 2019 Simone Caronni <negativo17@gmail.com> - 1:9.0.20-1
- Update to 9.0.20.

* Thu Jan 03 2019 Simone Caronni <negativo17@gmail.com> - 1:8.2.16-1
- Update to 8.2.16.

* Tue Apr 24 2018 Simone Caronni <negativo17@gmail.com> - 1:8.1.24-1
- Update to 8.1.24, do not add legacy samples.
- Update SPEC file.
- Require CUDA development package for 8.1.

* Thu Jun 22 2017 Simone Caronni <negativo17@gmail.com> - 1:8.0.14-1
- Update to 8.0.14.
- Do not add license also to samples, as it requires the base package.
- Requires driver 378.13+.
- Add NVDECODE headers and require nvidia-driver-devel for unversioned shared
  libraries.

* Sun Jan 08 2017 Simone Caronni <negativo17@gmail.com> - 1:7.1.9-1
- Update to 7.1.9.

* Fri Aug 19 2016 Simone Caronni <negativo17@gmail.com> - 7.0.1-1
- Update to 7.0.1.
- Runtime requires drivers 367.35+ and adds support for Pascal GPUs.

* Wed Jan 06 2016 Simone Caronni <negativo17@gmail.com> - 6.0.1-1
- Update to 6.0.1.

* Fri Apr 10 2015 Simone Caronni <negativo17@gmail.com> - 5.0.1-1
- First build.
