#include <stdio.h>
#include <string.h>
void addq(uint32_t *q, uint32_t v)
{
    q[++q[0]] = v;
}

uint32_t popq(uint32_t *q)
{
    if (!q[0])
        return -1;
    else return q[q[0]--];
}

void printq(uint32_t *q)
{
    printf("printq %d :", q[0]);
    for (int i = 0; i < q[0];i++)
        printf("%d ", q[i]);
    printf("\n");
}
int numIslands(char** grid, int gridRowSize, int gridColSize) 
{
    # define T(x) (x) / gridColSize][(x) % gridColSize
    #printf("%d %d\n", gridRowSize, gridColSize);
    uint8_t map[512 * 512];
    uint32_t q[512 * 512];
    uint32_t ret = 0;
    uint32_t temp;
    q[0] = 0;
    memset(map, 0, sizeof(map));
    for (int i = 0;i < gridColSize * gridRowSize; i++)
    {
        if (grid[T(i)] == '1' && !map[i])
        {
            ret += 1;
            addq(q, i);
            //printf("first %d\n",i);
            while (q[0])
            {
                temp = popq(q);
                map[temp] = 1;
                if (temp / gridColSize >= 1 && !map[temp - gridColSize] && grid[T(temp - gridColSize)] == '1')
                    addq(q, temp - gridColSize);
                if (temp % gridColSize != 0 && !map[temp - 1] && grid[T(temp - 1)] == '1')
                    addq(q, temp - 1);
                if ((temp + 1) % gridColSize != 0 && !map[temp + 1] && grid[T(temp + 1)] == '1')
                    addq(q, temp + 1);
                if (temp / gridColSize < gridRowSize - 1 && !map[temp + gridColSize] && grid[T(temp + gridColSize)] == '1')
                    addq(q, temp + gridColSize); 
                //printq(q);
            }
        }
    }
    return ret;
}