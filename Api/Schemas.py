from pydantic import BaseModel,Field
from typing import Annotated

class input_data(BaseModel):
    Time : Annotated[float,Field(...,gt = 0,description="Time in second from Fast transaction",example=25000)]
    Amount : Annotated[float,Field(...,description="Amount of money",example=100)]
    V1: Annotated[float,Field(...,description="pca transformed data",example=1.765285)]
    V2: Annotated[float,Field(...,description="pca transformed data",example=-1.863365)]
    V3: Annotated[float,Field(...,description="pca transformed data",example=1.235786)]
    V4: Annotated[float,Field(...,description="pca transformed data",example=0.287743)]
    V5: Annotated[float,Field(...,description="pca transformed data",example=-0.235371)]
    V6: Annotated[float,Field(...,description="pca transformed data",example=0.424123)]
    V7: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V8: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V9: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V10: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V11: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V12: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V13: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V14: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V15: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V16: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V17: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V18: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V19: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V20: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V21: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V22: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V23: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V24: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V25: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V26: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V27: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    V28: Annotated[float,Field(...,description="pca transformed data",example=1.23)]
    
    
    