#include "hello_world.h"
#include <iostream>

using namespace std;

namespace hello_world
{
string hello()
{
    return "Hello, World!";
   }

}


int mai ()
{
    string mot;
    mot = hello_world::hello();
    cout << mot;
    return 0;
}
