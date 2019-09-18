#!/usr/bin/env python3
# pylint: disable=missing-docstring,import-error,invalid-name

import ldap
import ldap3


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


def ldaptre():
    print("ldap3")
    server = ldap3.Server('ldaps://ldap.su.se', get_info=ldap3.ALL)
    conn = ldap3.Connection(
        server,
        auto_bind=True,
        authentication=ldap3.SASL,
        sasl_mechanism=ldap3.GSSAPI,
    )
    print("whoami: {}".format(conn.extend.standard.who_am_i()))
    conn.search(search_base='',
                search_scope=ldap3.SUBTREE,
                search_filter='(uid=simlu)',
                attributes=['eduPersonAffiliation'])
    print(conn.entries)


def main():
    python_ldap()
    print("")
    ldaptre()


if __name__ == "__main__":
    main()
