Name:           nvidia-sdk-video-codec
Version:        13.0.19
Release:        2%{?dist}
Epoch:          1
Summary:        A comprehensive set of APIs for hardware accelerated video encode and decode
License:        NVIDIA DesignWorks SDK License (v. May 10, 2022)
URL:            https://developer.nvidia.com/video-codec-sdk
BuildArch:      noarch

Source0:        Video_Codec_Interface_%{version}.zip
# From documentation at: https://docs.nvidia.com/video-technologies/index.html
Source1:        https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/pdf/License.pdf
Source2:        https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/pdf/Deprecation_Notices.pdf
Source3:        https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/pdf/Read_Me.pdf

Conflicts:      nvidia-video-codec-sdk

Obsoletes:      nvenc < %{?epoch}:%{version}-%{release}
Provides:       nvenc = %{?epoch}:%{version}-%{release}

# Required for:
# - libnvcuvid.so (NVDECODE)
# - libnvidia-encode.so (NVENCODE)
Requires:       nvidia-driver-cuda-libs >= 3:550.54.14

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
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%install
mkdir -p %{buildroot}%{_includedir}/%{name}/
install -m 644 -p Interface/* %{buildroot}%{_includedir}/%{name}/

%files
%license License.pdf
%doc Deprecation_Notices.pdf Read_Me.pdf
%{_includedir}/%{name}
 
%changelog
* Sun May 11 2025 Simone Caronni <negativo17@gmail.com> - 1:13.0.19-2
- Update to 13.0.19.

* Tue Sep 24 2024 Simone Caronni <negativo17@gmail.com> - 1:12.2.72-1
- Update to 12.2.72.
- Trim changelog.
- Add additional documentation.

* Tue Jun 13 2023 Simone Caronni <negativo17@gmail.com> - 1:12.1.14-1
- Update to 12.1.14.

* Mon Feb 06 2023 Simone Caronni <negativo17@gmail.com> - 1:12.0.16-1
- Update to 12.0.16.
- Switch to headers only package, drop samples.

* Wed Sep 22 2021 Simone Caronni <negativo17@gmail.com> - 1:11.1.5-1
- Update to 11.1.5.
