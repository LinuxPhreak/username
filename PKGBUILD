# Maintainer: Ben P. Dorsi-Todaro <ben@bigbenshosting.com>
_pkgbasename=username
pkgname=$_pkgbasename-git
pkgrel=1
pkgver=v1.0
pkgdesc="Get Username information"
arch=('any')
url="https://linuxphreak.github.io/username"
license=('GPL')
depends=('python3' 'python-requests' 'python-beautifulsoup4')
source=(git+https://github.com/LinuxPhreak/username)
md5sums=('SKIP')

pkgver() {
    cd "$srcdir/$_pkgbasename"
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
    cd "$srcdir/$_pkgbasename"
    
    python setup.py bdist
}


package() {
    _pkg=$(ls "$srcdir/$_pkgbasename/dist/")
    tar -xC "$pkgdir/" -f "$srcdir/$_pkgbasename/dist/$_pkg"

    mkdir -p "$pkgdir/usr/bin"

    _python=$(ls "$pkgdir/usr/lib/")
    cp $srcdir/$_pkgbasename/lib/$_python/site-packages/$_pkgbasename.py $pkgdir/usr/lib/$_python/site-packages/$_pkgbasename.py
    chmod +x "$pkgdir/usr/lib/$_python/site-packages/$_pkgbasename.py"
    ln -s "/usr/lib/$_python/site-packages/$_pkgbasename.py" "$pkgdir/usr/bin/username"

}