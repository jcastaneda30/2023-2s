class Node
{
public:
    int key;
    Node *left;
    Node *right;
    int height;

    Node(int key)
    {
        this->key = key;
        this->left = nullptr;
        this->right = nullptr;
        this->height = 1;
    }
};
#include <iostream>
using namespace std;

class AVLTree
{
public:
    int size;
    Node *root;

    AVLTree()
    {
        size = 0;
        root = nullptr;
    }

    void insert(int key)
    {
        if (!search(key))
        {
            root = _insertRecursively(root, key);
        }
    }

    Node *_insertRecursively(Node *root, int key)
    {
        if (!root)
        {
            Node *new_node = new Node(key);
            size++;
            return new_node;
        }
        else if (key < root->key)
        {
            root->left = _insertRecursively(root->left, key);
        }
        else
        {
            root->right = _insertRecursively(root->right, key);
        }

        root->height = 1 + max(_getNodeHeight(root->left), _getNodeHeight(root->right));

        int balanceFactor = _getNodeBalance(root);
        if (balanceFactor > 1)
        {
            if (key < root->left->key)
            {
                return _rightRotate(root);
            }
            else
            {
                root->left = _leftRotate(root->left);
                return _rightRotate(root);
            }
        }

        if (balanceFactor < -1)
        {
            if (key > root->right->key)
            {
                return _leftRotate(root);
            }
            else
            {
                root->right = _rightRotate(root->right);
                return _leftRotate(root);
            }
        }

        return root;
    }
    Node *_leftRotate(Node *z)
    {
        Node *y = z->right;
        Node *aux = y->left;
        y->left = z;
        z->right = aux;
        z->height = 1 + max(_getNodeHeight(z->left), _getNodeHeight(z->right));
        y->height = 1 + max(_getNodeHeight(y->left), _getNodeHeight(y->right));
        return y;
    }

    Node *_rightRotate(Node *z)
    {
        Node *y = z->left;
        Node *aux = y->right;
        y->right = z;
        z->left = aux;
        z->height = 1 + max(_getNodeHeight(z->left), _getNodeHeight(z->right));
        y->height = 1 + max(_getNodeHeight(y->left), _getNodeHeight(y->right));
        return y;
    }

    int _getNodeHeight(Node *root)
    {
        if (!root)
        {
            return 0;
        }
        return root->height;
    }

    int _getNodeBalance(Node *root)
    {
        if (!root)
        {
            return 0;
        }
        return _getNodeHeight(root->left) - _getNodeHeight(root->right);
    }

    int _getMin(Node *root)
    {
        if (!root)
        {
            return -1; // Otra opción sería retornar un valor que indique que no se encontró ningún valor mínimo.
        }
        else if (!root->left)
        {
            return root->key;
        }
        return _getMin(root->left);
    }

    bool search(int key)
    {
        return _searchRecursively(root, key) != nullptr;
    }

    Node *_searchRecursively(Node *root, int key)
    {
        if (!root || root->key == key)
        {
            return root;
        }
        if (key < root->key)
        {
            return _searchRecursively(root->left, key);
        }
        else
        {
            return _searchRecursively(root->right, key);
        }
    }
    Node *_searchRecursively(Node *root, int key)
    {
        if (!root || root->key == key)
        {
            return root;
        }
        if (key < root->key)
        {
            return _searchRecursively(root->left, key);
        }
        else
        {
            return _searchRecursively(root->right, key);
        }
    }

    vector<int> inOrder()
    {
        vector<int> elements;
        _inOrderRecursively(root, elements);
        return elements;
    }

    void _inOrderRecursively(Node *root, vector<int> &elements)
    {
        if (root)
        {
            _inOrderRecursively(root->left, elements);
            elements.push_back(root->key);
            _inOrderRecursively(root->right, elements);
        }
    }

    vector<int> PreOrderRaro(int altura)
    {
        vector<int> elements;
        vector<bool> visitados(size + 1, false); // size es el tamaño del árbol
        for (int i = 0; i <= altura; i++)
        {
            _PreOrderRaroRecursively(root, elements, i, visitados, 0);
        }
        return elements;
    }

    void _PreOrderRaroRecursively(Node *root, vector<int> &elements, int altura, vector<bool> &visitados, int actual)
    {
        if (root)
        {
            if (root->left && root->right && (actual == altura) && !visitados[root->key])
            {
                elements.push_back(2);
                visitados[root->key] = true;
            }
            else if (!root->left && !root->right && (actual == altura) && !visitados[root->key])
            {
                elements.push_back(0);
                visitados[root->key] = true;
            }
            else if (!root->left && (actual == altura) && !visitados[root->key])
            {
                elements.push_back(1);
                visitados[root->key] = true;
            }
            else if (!root->right && (actual == altura) && !visitados[root->key])
            {
                elements.push_back(-1);
                visitados[root->key] = true;
            }
            _PreOrderRaroRecursively(root->left, elements, altura, visitados, actual + 1);
            _PreOrderRaroRecursively(root->right, elements, altura, visitados, actual + 1);
        }
    }

    int popMin()
    {
        if (size == 0)
        {
            return -1; // Retorna un valor que indique que el árbol está vacío
        }
        else
        {
            int key = _getMin(root);
            deleteNode(key);
            return key;
        }
    }

    void deleteNode(int key)
    {
        root = _deleteRecursively(root, key);
    }

    Node *_deleteRecursively(Node *root, int key)
    {
        if (!root)
        {
            return root;
        }
        if (key < root->key)
        {
            root->left = _deleteRecursively(root->left, key);
        }
        else if (key > root->key)
        {
            root->right = _deleteRecursively(root->right, key);
        }
        else
        {
            if (!root->left || !root->right)
            {
                Node *temp = root->left ? root->left : root->right;
                if (!temp)
                {
                    temp = root;
                    root = nullptr;
                }
                else
                {
                    *root = *temp;
                }
                delete temp;
            }
            else
            {
                Node *temp = _getSuccessor(root->right);
                root->key = temp->key;
                root->right = _deleteRecursively(root->right, temp->key);
            }
        }

        if (!root)
        {
            return root;
        }

        root->height = 1 + max(_getNodeHeight(root->left), _getNodeHeight(root->right));
        int balance = _getNodeBalance(root);

        if (balance > 1 && _getNodeBalance(root->left) >= 0)
        {
            return _rightRotate(root);
        }
        if (balance > 1 && _getNodeBalance(root->left) < 0)
        {
            root->left = _leftRotate(root->left);
            return _rightRotate(root);
        }
        if (balance < -1 && _getNodeBalance(root->right) <= 0)
        {
            return _leftRotate(root);
        }
        if (balance < -1 && _getNodeBalance(root->right) > 0)
        {
            root->right = _rightRotate(root->right);
            return _leftRotate(root);
        }
        return root;
    }

    Node *_getSuccessor(Node *root)
    {
        while (root && root->left)
        {
            root = root->left;
        }
        return root;
    }

    // Otras funciones de apoyo (_getNodeHeight, _getNodeBalance, _rightRotate, _leftRotate) deben ser definidas
};
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    while (true)
    {
        int tamano;
        cin >> tamano;
        if (tamano == 0)
        {
            break;
        }

        AVLTree avl;
        for (int i = 0; i < tamano; i++)
        {
            int dato;
            cin >> dato;
            avl.insert(dato);
        }

        vector<int> inOrderResult = avl.inOrder();
        int altura = *max_element(inOrderResult.begin(), inOrderResult.end());

        vector<int> valores = avl.PreOrderRaro(altura);
        for (int i = 0; i < valores.size(); i++)
        {
            cout << valores[i];
            if (i < valores.size() - 1)
            {
                cout << ".";
            }
        }
        cout << endl;
    }

    return 0;
}
