class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

#init node
head = ListNode(0)
nHead = head
for i in range(10):
	head.next = ListNode(i+1)
	head = head.next

#print the nodes for verification

p, i = nHead.next, 0
nums = []
while p:
	nums.append(p.val)
	p, i = p.next, i+1
print(nums)

############# begin the coding #################

current = nHead.next
pnext = current.next
current.next = None
while pnext:
	prev = pnext.next
	pnext.next = current
	current = pnext
	pnext = prev
nHead.next = current

p, i = nHead.next, 0
nums = []
while p:
	if i>100:
		break
	nums.append(p.val)
	p, i = p.next, i+1
print(nums)

