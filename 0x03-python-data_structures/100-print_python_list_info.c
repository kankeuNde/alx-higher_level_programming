#include "Python.h"

/**
 * print_python_list_info - Prints information about objects
 * @p: PyObject pointer to print info about
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t index, py_l_size;
	PyObject *item;
	const char *item_type;
	PyListObject *plo;

	plo = (PyListObject *)p;
	py_l_size = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", (int)py_l_size);
	printf("[*] Allocated = %d\n", (int)plo->allocated);
	for (index = 0; inde < py_l_size; index++)
	{
		item = PyListList_GetItem(p, index);
		item_type = Py_TYPE(item)->tp_name;
		printf("Element %d: %s\n", (int) index, item_type);
	}
}
