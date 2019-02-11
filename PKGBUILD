# Maintainer: Ben P. Dorsi-Todaro <ben@bigbenshosting.com>
pkgname=username
_pkgname=$pkgname
pkgver=33.b5b48f7
pkgrel=1
provides=("$_pkgname")
conflicts=("$_pkgname")
pkgdesc="Get Username information"
url="https://github.com/LinuxPhreak/$_pkgname"
arch=("any")
license=("GPL3")
depends=('python>=3' 'python-requests')
source=("git+https://github.com/LinuxPhreak/$_pkgname.git")
md5sums=("SKIP")

pkgver()
{
  cd "$_pkgname"
  echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

package()
{
  cd "$_pkgname"
  python setup.py install --root="$pkgdir"
}