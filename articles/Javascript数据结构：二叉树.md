## 二叉树：每个节点最多有两个子节点。
~~~
	  10
	/    \
	9    20
			/   \
	   15   35
~~~

## 二叉树的特点：
1. 每个节点最多有两个子树，节点的度最大为2；
2. 左子树和右子树是有顺序的，次序不能颠倒；
3. 即使某节点只有一个子树，也要区分左右子树；

## 二叉树的操作：
1. 创建二叉树；
2. 遍历二叉树；
	a. 先序遍历：先访问根节点，然后访问左节点，最后访问右节点（根->左->右）10->9->20->15->35
	b. 中序遍历：先访问左节点，然后访问根节点，最后访问右节点（左->根->右）9->10->15->20->35
	c. 后序遍历：先访问左节点，然后访问右节点，最后访问根节点（左->右->根）9->15->35->20->10
3. 查询树的深度；
4. 查询树的最大值；

通过先序和中序/中序和后序我们可以还原出原始的二叉树，但是通过先序和后序是无法还原出原始的二叉树的。（？）

## 特殊的二叉树：
1. 斜树；
所有的节点都只有左子树（左斜树），后者只有右子树（右斜树）。

2. 满二叉树；
所有的分支节点都存在左子树和右子树，并且所有的叶子结点都在同一层上。

满二叉树的特点：
a. 叶子只能出现在最下一层；
b. 非叶子节点度一定是2；
c. 在同样深度的二叉树中，满二叉树的节点个数最多，叶子树最多；

3. 完全二叉树；
对一棵具有n个结点的二叉树按层序排号，如果编号为i的结点与同样深度的满二叉树编号为i结点在二叉树中位置完全相同，就是完全二叉树。
满二叉树必须是完全二叉树，反过来不一定成立。

完全二叉树特点：
a. 叶子节点只能出现在最下一层（满二叉树继承而来）；
b. 最下层叶子节点一定集中在左 部连续位置；
c. 倒数第二层，如有叶子节点，一定出现在右部连续位置；
d. 同样节点树的二叉树，完全二叉树的深度最小（满二叉树也是对的）；

二叉查找树(binary search tree)：
当前根节点的左边全部比根节点小，当前根节点的右边全部比根节点大。

## 二叉树题目:
(01) 求二叉树的最大深度；
(02) 求二叉树的最小深度；
(03) 求二叉树中节点的个数；
(04) 求二叉树中叶子节点的个数；
(05) 求二叉树中第k层节点的个数；
(06) 判断二叉树是否是平衡二叉树；
(07) 判断二叉树是否是完全二叉树；
(08) 判断两个二叉树是否完全相同；
(09) 判断两个二叉树是否互为镜像；
(10) 翻转二叉树/镜像二叉树；
(11) 求两个二叉树的最低公共祖先节点；
(12) 二叉树的前序遍历；
(13) 二叉树的中序遍历；
(14) 二叉树的后序遍历；
(15) 构造二叉树（前序遍历和中序遍历/后序遍历和中序遍历）；
(16) 二叉树中插入/删除节点；
(17) 输入一个二叉树和一个整数，打印出二叉树中节点值的和等于输入整数所有的路径；
(18) 二叉树的搜索区间；
(19) 二叉树的层次遍历；
(20) 二叉树内两个节点的最长距离；
(21) 不同的二叉树；
(22) 判断二叉树是否是合法的二叉查找树（BST）；


## 二叉树操作：
1. 前序遍历，中序遍历，后序遍历；
2. 层次遍历；
3. 求树的节点数；
4. 求树的叶子数；
5. 求树的深度；
6. 求二叉树第k层的节点个数;
7. 判断两棵二叉树是否结构相同；
8. 求二叉树的镜像；
9. 求两个节点的最低公共祖先节点；
10. 求任意两节点距离；
11. 找出二叉树中某个节点的所有祖先节点；
12. 不使用递归和栈遍历二叉树；
13. 二叉树前序中序推后序；
14. 判断二叉树是不是完全二叉树;
15. 判断是否是二叉查找树的后序遍历结果；
16. 给定一个二叉查找树中的节点，找出在中序遍历下它的后继和前驱；
17. 二分查找树转化为排序的循环双链表；
18. 有序链表转化为平衡的二分查找树。

~~~
class TreeNode {
	constructor(data) {
    this.data = data;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree {
	constructor() {
		this.root = null;
    this.inorderList = [];
  }

  // 插入数据
  insert(data){
  	var newNode = new TreeNode(data);
  	if(this.root === null){
  		this.root = newNode;
  	}else{
  		this.insertNode(this.root,newNode);
  	}
  }

  // 插入节点
  insertNode(node,newNode){
  	if(newNode.data < node.data){
  		if(node.left === null){
  			node.left = newNode;
  		}else{
  			this.insertNode(node.left, newNode);
  		}
  	}else{
  		if(node.right === null){
  			node.right = newNode;
  		}else{
  			this.insertNode(node.right, newNode);
  		}
  	}
  }

  // 删除数据
  remove(data){
  	this.root = this.removeNode(this.root,data);
  }

  // 删除节点
  removeNode(node,data){
  	if(node === null){
  		return null;
  	}else if(data < node.data){
  		node.left = this.removeNode(node.left,data);
  		return node;
  	}else if(data > node.data){
  		node.right = this.removeNode(node.right,data);
  		return node;
  	}else{
  		if(node.left === null && node.right === null){
  			node = null;
  			return node;
  		}
  		if(node.left === null){
  			node = node.right;
  			return node;
  		}else if(node.right === null){
  			node = node.left;
  			return node;
  		}
  		// Deleting node with two children
      // minumum node of the rigt subtree
      // is stored in aux
      var aux = this.findMinNode(node.right);
      node.data = aux.data;

      node.right = this.removeNode(node.right, aux.data);
      return node;
  	}
  }

  // 查找最小节点（如果左节点为空，那么它一定是最小节点）
  findMinNode(node){
  	if(node.left === null){
  		return node;
  	}else{
  		return this.findMinNode(node.left);
  	}
  }

  // 获取根节点
  getRootNode(){
  	return this.root;
  }

  //中序遍历（左->根->右）
  inorder(node){ 
  	if(node != null){
  		this.inorder(node.left);
  		console.log(node.data);
      this.inorderList.push(node.data);
  		this.inorder(node.right);
  	}
  }

  //前序遍历（根->左->右）
  preorder(node){ 
  	if(node != null){
  		console.log(node.data);
  		this.preorder(node.left);
  		this.preorder(node.right);
  	}
  } 

  //后序遍历（左->右->根）
  postorder(node){ 
  	if(node != null){
  		this.postorder(node.left);
  		this.postorder(node.right);
  		console.log(node.data);
  	}
  }

  search(node,data){
  	if(node === null){
  		return null;
  	}else if(data < node.data){
  		return this.search(node.left,data);
  	}else if(data > node.data){
  		return this.search(node.right,data);
  	}else{
  		return node;
  	}
  }

  // 获取二叉树的最大深度
  getMaxDepth(node){
    if(node === null){
      return 0;
    }
    var left = this.getMaxDepth(node.left);
    var right = this.getMaxDepth(node.right);
    return Math.max(left,right) + 1;
  }

  // 获取二叉树的最小深度（对树进行层序遍历，找到第一个左右都为NULL情况，返回当前树的高度。）
  getMinDepth(node){
    if(node == null){
      return 0;
    }
    if(node.left === null && node.right === null){
      return 1;
    }
    if(node.left === null){
      return this.getMinDepth(node.right) + 1;
    }else if(node.right === null){
      return this.getMinDepth(node.left) + 1;
    }else{
      return Math.min(this.getMinDepth(node.left),this.getMinDepth(node.right)) + 1;
    }
  }

  // 获取二叉树中节点的个数
  getNumberOfNode(node){
    if(node === null){
      return 0;
    }
    var left = this.getNumberOfNode(node.left);
    var right = this.getNumberOfNode(node.right);
    return left + right + 1;
  }

  // 获取二叉树中叶子节点的个数
  getNumerOfLeafNode(node){
    if(node === null){
      return 0;
    }
    if(node.left === null && node.right === null){
      return 1;
    }
    return this.getNumerOfLeafNode(node.left) + this.getNumerOfLeafNode(node.right);
  }

  // 获取二叉树中第K层节点的个数？ / 叶子节点的个数呢？
  getNumberOfKLevelNode(node,k){
    if(node === null || k < 1){
      return 0;
    }
    if(k === 1){
      return 1;
    }
    var left = this.getNumberOfKLevelNode(node.left,k-1);
    var right = this.getNumberOfKLevelNode(node.right,k-1);
    return left + right;
  }

  // 判断二叉树是否是平衡二叉树
  isBalanceTree(node){
    return this.getDepth(node) != -1
  }

  getDepth(node){
    if(node === null){
      return 0;
    }
    var left = this.getDepth(node.left);
    var right = this.getDepth(node.right);
    if(left === -1 || right === -1 || Math.abs(left-right) > 1){
      return -1;
    }
    return Math.max(left,right) + 1;
  }



  /* 获取二叉树内两个节点的最长距离
   * 二叉树中两个节点的最长距离可能有三种情况：
   * 1.左子树的最大深度+右子树的最大深度为二叉树的最长距离
   * 2.左子树中的最长距离即为二叉树的最长距离
   * 3.右子树种的最长距离即为二叉树的最长距离
   */
  getMaxDistance(node){
    if(node === null){
      return 0;
    }
    


  }

  /* 判断二叉树是否是二叉查找树
   * 二叉搜索树的中序遍历是一个递增序列，所以我们只需要把这个中序遍历保存下来，然后判断这是个递增序列即可
   */
  isBST(node){
    var inorderList = this.inorderList;
    for(var i = 0; i < inorderList.length - 1; i ++){
      if(inorderList[i] < inorderList[i++]){
        return false;
      }
    }
    return true;
  }
}
~~~

~~~
// 给出 n，问由 1...n 为节点组成的不同的二叉查找树有多少种？ ???
// function numberOfTrees(n){
//   var counts = [];
//   counts[0] = 1;
//   counts[1] = 1;
//   for(var i = 2; i <= n; i++){
//     for(var j = 0; j < i; j++){
//       counts[i] = counts[j] * counts[i-j-1];
//     }
//   }
//   console.log(counts)
//   return counts[n];
// }

var BST = new BinarySearchTree();

BST.insert(15);
BST.insert(25);
BST.insert(10);
BST.insert(7);
BST.insert(22);
BST.insert(17);
BST.insert(13);
BST.insert(5);
BST.insert(9);
BST.insert(27);

//          15
//         /  \
//        10   25
//       / \   / \
//      7  13 22  27
//     / \    /
//    5   9  17 


var root = BST.getRootNode();

var maxDepth = BST.getMaxDepth(root); 
console.log(maxDepth) // 4 

var minDepth = BST.getMinDepth(root); 
console.log(minDepth) // 3

var numerOfNode = BST.getNumberOfNode(root); 
console.log(numerOfNode) // 10

var numberOfLeafNode = BST.getNumerOfLeafNode(root);
console.log(numberOfLeafNode) // 5

console.log(BST.getNumberOfKLevelNode(root,0)); // 0;
console.log(BST.getNumberOfKLevelNode(root,1)); // 1;
console.log(BST.getNumberOfKLevelNode(root,2)); // 2;
console.log(BST.getNumberOfKLevelNode(root,3)); // 4;
console.log(BST.getNumberOfKLevelNode(root,4)); // 3;

var isBST = BST.isBST(root); 
console.log(isBST);  // true

var isBalanceTree = BST.isBalanceTree(root);
console.log(isBalanceTree);

~~~

## 二叉树确定
~~~
class TreeNode {
	constructor(data) {
    this.data = data;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree {
	constructor() {
		this.root = null;
  }

  insert(data){
  	var newNode = new TreeNode(data);
  	if(this.root === null){
  		this.root = newNode;
  	}else{
  		this.insertNode(this.root,newNode);
  	}
  }

  insertNode(node,newNode){
  	if(newNode.data < node.data){
  		if(node.left === null){
  			node.left = newNode;
  		}else{
  			this.insertNode(node.left, newNode);
  		}
  	}else{
  		if(node.right === null){
  			node.right = newNode;
  		}else{
  			this.insertNode(node.right, newNode);
  		}
  	}
  }

  remove(data){
  	this.root = this.removeNode(this.root,data);
  }

  removeNode(node,data){
  	if(node === null){
  		return null;
  	}else if(data < node.data){
  		node.left = this.removeNode(node.left,data);
  		return node;
  	}else if(data > node.data){
  		node.right = this.removeNode(node.right,data);
  		return node;
  	}else{
  		if(node.left === null && node.right === null){
  			node = null;
  			return node;
  		}
  		if(node.left === null){
  			node = node.right;
  			return node;
  		}else if(node.right === null){
  			node = node.left;
  			return node;
  		}
  		// Deleting node with two children
      // minumum node of the rigt subtree
      // is stored in aux
      var aux = this.findMinNode(node.right);
      node.data = aux.data;

      node.right = this.removeNode(node.right, aux.data);
      return node;
  	}
  }

  findMinNode(node){
  	if(node.left === null){
  		return node;
  	}else{
  		return this.findMinNode(node.left);
  	}
  }

  getRootNode(){
  	return this.root;
  }

  inorder(node){ //中序（左->根->右）
  	if(node != null){
  		this.inorder(node.left);
  		console.log(node.data);
  		this.inorder(node.right);
  	}
  }

  preorder(node){ //前序（根->左->右）
  	if(node != null){
  		console.log(node.data);
  		this.preorder(node.left);
  		this.preorder(node.right);
  	}
  } 

  postorder(node){ //后序（左->右->根）
  	if(node != null){
  		this.postorder(node.left);
  		this.postorder(node.right);
  		console.log(node.data);
  	}
  }

  search(node,data){
  	if(node === null){
  		return null;
  	}else if(data < node.data){
  		return this.search(node.left,data);
  	}else if(data > node.data){
  		return this.search(node.right,data);
  	}else{
  		return node;
  	}
  }
}
~~~

//前序（根->左->右）
//中序（左->根->右）
//后序（左->右->根）

//已知前序和中序，可以唯一确定一棵二叉树。
//已知后序和中序，可以唯一确定一棵二叉树。

//已知前序和后序，为什么不能唯一确定一棵二叉树？

~~~
var BST = new BinarySearchTree();
BST.insert(15);
BST.insert(25);
BST.insert(10);
BST.insert(7);
BST.insert(22);
BST.insert(13);
//          15
//         /  \
//        10   25
//       / \   / 
//      7  13 22  

var root = BST.getRootNode();

console.log('前序');//（根->左->右）
BST.preorder(root); // (15) 10 7 13 25 22 

console.log('中序');//（左->根->右）
BST.inorder(root); // 7 10 13 (15) 22 25 

console.log('后序');//（左->右->根）
BST.postorder(root); // 7 13 10 22 25 15 
~~~

1) 由前序得出：
   根节点： 15
   根节点的左孩子：10

2) 由中序得出：
   左子树节点 - 根节点 - 右子树节点
   （7 10 13）- 15 -（22 25）
~~~
//       15
//      /   \
//    10     25
//   /  \    /
//  7   13  22
~~~

3) 由后序得出：
   根节点： 15
   根节点的右孩子：25


参考：
https://segmentfault.com/a/1190000008850005
http://www.cnblogs.com/polly333/p/4740355.html