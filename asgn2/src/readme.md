getreg(lineno,var):
first check if there is any destination involved or not. Though it might not be reqd bt lets see if nt we  will remove it

second division mod or non division which is currently TODO item

if not then what it does is ki it simply allocates a register to the var specefied.
How??
first check if there is some reg which is yet to be assigned. if there is , then return that

if not then check if there is any var in reg which is not having any next use. If we find one such reg, we save it in memory and allocate this reg to var

else we then iterate through all the registers in nextuse and find the the variable currently assigned a reg having its farthest use. We then move this reg's value back in memory and then we will assign this register to the var


a lot is left to be done
