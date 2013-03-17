cdef extern from "blosc_filter.h":
   int register_blosc(char **version, char **date)

cpdef register():
    cdef:
        char *version
        char *date
    register_blosc(&version, &date)
