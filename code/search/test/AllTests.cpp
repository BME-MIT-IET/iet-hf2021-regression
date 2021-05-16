#include "CppUTest/CommandLineTestRunner.h"

int main(int argc, char **argv)
{
    int rc = CommandLineTestRunner::RunAllTests(argc, argv);
    return rc;
}
