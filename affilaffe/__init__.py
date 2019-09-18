#!/usr/bin/env python3
# pylint: disable=missing-docstring,import-error,invalid-name

import ldap
import ldap.sasl


def python_ldap():
    print("python-ldap")
    l = ldap.initialize("ldaps://ldap.su.se")  # noqa: E741

    l.sasl_gssapi_bind_s()
    print("whoami: {}".format(l.whoami_s()))

    result = l.search_s(base="",
                        scope=ldap.SCOPE_SUBTREE,
                        filterstr="(uid=simlu)",
                        attrlist=["eduPersonAffiliation"])
    print(result)


def main():
    python_ldap()
    print("")


if __name__ == "__main__":
    main()
